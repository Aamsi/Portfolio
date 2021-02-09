<template>
    <v-container fluid>
        <v-row align="center">
            <v-col
            class="d-flex mx-auto"
            cols="12"
            >
                <v-select
                    :items="categories"
                    label="Categorie"
                    filled
                    outlined
                    @change="sortProjects"
                ></v-select>
            </v-col>
        </v-row>

        <v-row dense>
            <v-col
                v-for="project in activeProjects"
                :key="project.title"
            >
                <Project
                    :image="project.picture"
                    :title="project.title"
                    :description="project.description"
                    :url="project.url"
                />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import Project from '../components/Project'
import { mapState } from "vuex"

export default {
    name: 'Projects',
    components: {
        Project,
    },
    data () {
        return {
            activeProjects: []
        }
    },
    computed: {
        ...mapState({
            categories: "categories",
            projects: 'projects'
        }),
    },
    methods: {
        sortProjects(category) {
            this.activeProjects = [];
            if (category == "Tous")
                return (this.activeProjects = this.projects);

            for (let project of this.projects) {
                for (let cat of project.categories) {
                    if (cat.name == category) {
                        this.activeProjects.push(project);
                        break;
                    }
                }
            }
        },
    },
    created () {
        this.$store.dispatch('loadCategories');
        this.$store.dispatch('loadProjects');

        this.activeProjects = this.projects;
    },

}
</script>
