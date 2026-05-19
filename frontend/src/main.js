// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
// 导入路由配置文件（重点：路由要单独配置）
import router from './router/index.js' 

// 创建Vue实例并挂载路由
const app = createApp(App)
app.use(router)
app.mount('#app')