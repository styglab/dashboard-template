import reflex as rx
from reflex import Color
from reflex.experimental import ClientStateVar
#
from ..ui.main import main_page
from .. import navigation
#
#
def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/#"),
        sidebar_item("Projects", "square-library", "/#"),
        sidebar_item("Analytics", "bar-chart-4", "/#"),
        sidebar_item("Messages", "mail", "/#"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                "RA",
                class_name="text-white font-bold text-lg mr-2 p-2 bg-blue-600 rounded",
            ),
            rx.el.div(
                rx.el.p(
                    "Retail analytics",
                    class_name="font-semibold",
                ),
                rx.el.p(
                    "Member",
                    class_name="text-xs text-gray-500",
                ),
                class_name="flex-grow",
            ),
            rx.el.button(
                rx.icon(tag="chevron_down", size=16),
                variant="ghost",
                class_name="text-gray-600 hover:text-gray-900",
            ),
            class_name="flex items-center p-4 border-b border-gray-200",
        ),
        rx.el.nav(
            rx.el.a(
                rx.icon(
                    tag="layout_dashboard",
                    size=18,
                    class_name="mr-3",
                ),
                "Overview",
                href="#",
                class_name="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded",
            ),
            rx.el.a(
                rx.icon(tag="list", size=18, class_name="mr-3"),
                "Details",
                href="#",
                class_name="flex items-center px-4 py-2 text-sm font-medium text-blue-600 bg-blue-50 rounded",
            ),
            rx.el.a(
                rx.icon(
                    tag="settings",
                    size=18,
                    class_name="mr-3",
                ),
                "Settings",
                href="#",
                class_name="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded",
            ),
            rx.el.div(
                rx.el.h3(
                    "Shortcuts",
                    class_name="px-4 pt-4 pb-2 text-xs font-semibold text-gray-500 uppercase",
                ),
                rx.el.a(
                    rx.icon(
                        tag="plus",
                        size=16,
                        class_name="mr-3",
                    ),
                    "Add new user",
                    href="#",
                    class_name="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded",
                ),
                rx.el.a(
                    rx.icon(
                        tag="briefcase",
                        size=16,
                        class_name="mr-3",
                    ),
                    "Workspace usage",
                    href="#",
                    class_name="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded",
                ),
                rx.el.a(
                    rx.icon(
                        tag="credit_card",
                        size=16,
                        class_name="mr-3",
                    ),
                    "Cost spend control",
                    href="#",
                    class_name="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded",
                ),
                rx.el.a(
                    rx.icon(
                        tag="file_text",
                        size=16,
                        class_name="mr-3",
                    ),
                    "Overview - Rows written",
                    href="#",
                    class_name="flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 rounded",
                ),
            ),
            class_name="flex-grow p-4 space-y-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "ES",
                    class_name="w-8 h-8 rounded-full bg-gray-300 flex items-center justify-center text-sm font-medium text-gray-700 mr-3",
                ),
                rx.el.p(
                    "Emma Stone",
                    class_name="text-sm font-medium text-gray-800 flex-grow",
                ),
                rx.el.button(
                    rx.icon(tag="send_horizontal", size=16),
                    variant="ghost",
                     
                     
                ),
                class_name="flex items-center p-4",
            ),
            class_name="border-t border-gray-200",
        ),
        class_name="w-64 border-r border-gray-200 flex flex-col h-screen",
    )



@rx.page(route=navigation.routes.SIDEBAR_PAGE_ROUTE)
def sidebar_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = sidebar()
    return main_page(my_child)

