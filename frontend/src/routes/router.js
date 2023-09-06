import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter)

import Produtos from '@/pages/Produtos'

const routes = [
    {
        path: '/',
        component: Produtos,
    },
]

const router = new VueRouter({
    routes,
    mode:'history'
})

export default router