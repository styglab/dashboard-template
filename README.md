## reflex-template

#### 1. uv
uv sync --frozen --no-install-project --no-dev
source .venv/bin/activate

#### 2. reflex
reflex run


#### (dev)
uv init --python 3.12
uv add -r requirements.txt
source .venv/bin/activate
reflex init
###### db init
(최초)
reflex db init
(db모델 변경 시)
reflex db makemigrations
reflex db migrate

