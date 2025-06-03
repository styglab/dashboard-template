import reflex as rx
from typing import List, Optional
from sqlmodel import select
from datetime import datetime, timezone, timedelta
#
from .model import BlogPostModel
from .. import navigation
#
#
BLOG_POSTS_ROUTE = navigation.routes.BLOG_POSTS_ROUTE
if BLOG_POSTS_ROUTE.endswith("/"):
    BLOG_POSTS_ROUTE = BLOG_POSTS_ROUTE[:-1]

class BlogPostState(rx.State):
    posts: List[BlogPostModel] = []
    post: Optional[BlogPostModel] = None
    post_content: str = ""
    post_publish_active: bool = False
    
    @rx.var
    def blog_post_id(self) -> str:
        #print(self.router.page.params)
        return self.router.page.params.get("blog_id", "")
    
    @rx.var
    def blog_post_url(self) -> str:
        if not self.post:
            return f"{BLOG_POSTS_ROUTE}"
        return f"{BLOG_POSTS_ROUTE}/{self.post.id}"

    @rx.var
    def blog_post_edit_url(self) -> str:
        if not self.post:
            return f"{BLOG_POSTS_ROUTE}"
        return f"{BLOG_POSTS_ROUTE}/{self.post.id}/edit"

    def load_posts(self, published_only=False):
        lookup_args = ()
        if published_only:
            lookup_args = (
                (BlogPostModel.publish_active == True) &
                (BlogPostModel.publish_date < datetime.now(timezone(timedelta(hours=9))))
            )
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel).where(*lookup_args)
            ).all()
            self.posts = result
            
    def add_post(self, form_data:dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            session.add(post)
            session.commit()
            session.refresh(post) # post.id
            print("added", post)
            self.post = post
            
    def get_post_detail(self):
        with rx.session() as session:
            if self.blog_post_id == "":
                self.post = None
                return
            result = session.exec(
                select(BlogPostModel).where(
                    BlogPostModel.id == self.blog_post_id
                )
            ).one_or_none()
            self.post = result
            if result is None:
                self.post_content = ""
                return
            self.post_content = self.post.content
            self.post_publish_active = self.post.publish_active
            
    def save_post_edits(self, post_id:int, updated_data:dict):
        with rx.session() as session:
            post = session.exec(
                select(BlogPostModel).where(
                    BlogPostModel.id == post_id
                )
            ).one_or_none()
            if post is None:
                return
            for key, value in updated_data.items():
                setattr(post, key, value) # post.title = updated_data.get("title") ..
                session.add(post)
                session.commit()
                session.refresh(post)
                self.post = post
                
    def to_blog_post(self, edit_page=False):
        if not self.post:
            return rx.redirect(BLOG_POSTS_ROUTE)
        if edit_page:
            return rx.redirect(f"{self.blog_post_edit_url}")
        return rx.redirect(f"{self.blog_post_url}")

class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}
    
    def handle_submit(self, form_data):
        self.form_data = form_data
        self.add_post(form_data)
        return self.to_blog_post(edit_page=True) # redirect
        
class BlogEditFormState(BlogPostState):
    form_data: dict = {}
    
    @rx.var
    def publish_display_date(self) -> str:
        # return "2025-01-01" # YYYY-MM-DD
        if not self.post:
            return datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d")
        if not self.post.publish_date:
            return datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d")
        return self.post.publish_date.strftime("%Y-%m-%d")
        
    @rx.var
    def publish_display_time(self) -> str:
        if not self.post:
            return datetime.now(timezone(timedelta(hours=9))).strftime("%H:%M:%S")
        if not self.post.publish_date:
            return datetime.now(timezone(timedelta(hours=9))).strftime("%H:%M:%S")
        return self.post.publish_date.strftime("%H:%M:%S")
    
    def handle_submit(self, form_data):
        self.form_data = form_data
        post_id = form_data.pop('post_id')
        publish_date = None
        if 'publish_date' in form_data:
            publish_date = form_data.pop('publish_date')
        publish_time = None
        if 'publish_time' in form_data:
            publish_time = form_data.pop('publish_time')
        print(publish_date, publish_time)
        publish_input_string = f"{publish_date} {publish_time}"
        try:
            final_publish_date = datetime.strptime(publish_input_string, '%Y-%m-%d %H:%M:%S')
        except:
            final_publish_date = None
        publish_active = False
        if 'publish_active' in form_data:
            publish_active = form_data.pop('publish_active') == 'on'
        updated_data = {**form_data}
        updated_data['publish_active'] = publish_active
        updated_data['publish_date'] = final_publish_date
        self.save_post_edits(post_id, updated_data)
        return self.to_blog_post() # redirect