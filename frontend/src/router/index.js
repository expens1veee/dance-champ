import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/registration',
            name: 'registration',
            component: () => import('../views/RegistrationView.vue')
        },
        {
            path: '/master-classes',
            name: 'master-classes',
            component: () => import('../views/MasterClassesView.vue')
        },
        {
            path: '/nominations',
            name: 'nominations',
            component: () => import('../views/NominationsView.vue')
        },
        {
            path: '/nominations/:slug',
            name: 'nomination-detail',
            component: () => import('../views/NominationDetailView.vue'),
            props: true
        },
        {
            path: '/kgo',
            name: 'kgo',
            component: () => import('../views/KGOView.vue') // Команда Главного Организатора
        },
        {
            path: '/regulations',
            name: 'regulations',
            component: () => import('../views/RegulationsView.vue') // Положение
        },
        {
            path: '/contacts',
            name: 'contacts',
            component: () => import('../views/ContactsView.vue')
        },
        {
            path: '/:pathMatch(.*)*',
            name: 'not-found',
            component: () => import('../views/NotFoundView.vue')
        }
    ]
})

export default router