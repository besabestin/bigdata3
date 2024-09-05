import { createRouter, createWebHistory } from 'vue-router'
import NeedToBuy from '@/views/NeedToBuy.vue';
import History from '@/views/History.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/need-to-buy' },
    { path: '/need-to-buy', component: NeedToBuy },
    { path: '/history', component: History }
  ]
})

export default router
