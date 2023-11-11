import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'


import Courses from '../views/Courses.vue'
import Course from '../views/Course.vue'
import Projects from '../views/Projects.vue'
import Project from '../views/Project.vue'


import MyAccount from '../views/dashboard/MyAccount.vue'
import CreateCourse from '../views/dashboard/CreateCourse.vue'
import Author from '../views/Author.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/courses',
    name: 'Courses',
    component: Courses
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects
  },
  {
    path: '/projects/:slug',
    name: 'Project',
    component: Project 
  },
  {
    path: '/courses/:slug',
    name: 'Course',
    component: Course
  },
  {
    path: '/authors/:id',
    name: 'Author',
    component: Author
  },

  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount
  },
  {
    path: '/dashboard/create-course',
    name: 'CreateCourse',
    component: CreateCourse
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
