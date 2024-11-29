import { createRouter, createWebHistory } from 'vue-router'
import NeedToBuy from '@/views/NeedToBuy.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: NeedToBuy
    },
    {
      path: '/history',
      name: 'history',
      component: () => import('../views/History.vue')
    },
    {
      path: '/listings',
      name: 'listings',
      component: () => import('../views/NeedToBuy.vue')
    }
  ]
})

export default router
