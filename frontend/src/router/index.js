import Vue from 'vue'
import VueRouter from 'vue-router'
import About from '../views/About.vue'
import Projects from '../views/Projects.vue'
import Admin from '../views/Admin.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects,
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
  }
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

export default router
