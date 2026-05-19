from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 初始化 FastAPI 应用
app = FastAPI(
    title="遥感目标智能检测平台",
    description="基于YOLO的遥感检测API",
    version="1.0.0"
)

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 健康检查接口（教程必须要）
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# 欢迎接口
@app.get("/")
def root():
    return {"message": "遥感检测平台已启动"}