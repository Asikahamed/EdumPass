<template>
    <div class="projects">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Projects</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-2">
                        <aside class="menu">
                            <p class="menu-label">Categories</p>

                            <ul class="menu-list">
                                <li>
                                    <a 
                                        v-bind:class="{'is-active': !activeCategory}"
                                        @click="setActiveCategory(null)"
                                    >
                                        All projects
                                    </a>
                                </li>
                                <li
                                    v-for="category in categories"
                                    v-bind:key="category.id"
                                    @click="setActiveCategory(category)"
                                >
                                    <a>{{ category.title }}</a>
                                </li>
                            </ul>
                        </aside>
                    </div>

                    <div class="column is-10">
                        <div class="columns is-multiline">
                            <div 
                                class="column is-4"
                                v-for="project in projects"
                                v-bind:key="project.id"
                            >
                                <ProjectItem :project="project" />
                            </div>

                            <div class="column is-12">
                                <nav class="pagination">
                                    <a class="pagination-previous">Previous</a>
                                    <a class="pagination-next">Next</a>
                                </nav>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios'
import ProjectItem from '@/components/ProjectItem.vue'

export default {
    data() {
        return {
            projects: [],
            categories: [],
            activeCategory: null
        }
    },
    components: {
        ProjectItem
    },
    async mounted() {
        document.title = 'Projects | EdumPass'

        await axios
            .get('projects/get_categories/')
            .then(response => {
                this.categories = response.data
            })
        
        this.getProjects()
    },
    methods: {
        setActiveCategory(category) {
            this.activeCategory = category
            this.getProjects()
        },
        getProjects() {
            let url = 'projects/'

            if (this.activeCategory) {
                url += '?category_id=' + this.activeCategory.id
            }

            axios
                .get(url)
                .then(response => {
                    this.projects = response.data
                })
        }
    }
}
</script>
