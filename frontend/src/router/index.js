// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
// 导入你实际创建的 Detection.vue 页面（不是 index.vue）
import Detection from "../views/Detection.vue"; 

const routes = [
  {
    path: "/",
    name: "detection",
    component: Detection, // 指向正确的页面文件
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;