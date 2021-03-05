<template>
    <v-container>
        <v-row align="center">
            <v-col
            class="d-flex mx-auto"
            cols="6"
            >
                <v-select
                    :items="categories"
                    v-model="defaultSelect"
                    label="Categorie"
                    filled
                    outlined
                    @change="sortProjects"
                    class="mt-15"
                ></v-select>
            </v-col>
        </v-row>

        <v-row dense>
            <v-col
                v-for="project in activeProjects"
                :key="project.title"
                :cols="cols"
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

export default {
    name: 'Projects',
    components: {
        Project,
    },
    data () {
        return {
            activeProjects: [],
            defaultSelect: "Tous",
            categories: ["Tous"],
            projects: [],
        }
    },
    computed: {
        cols () {
            if (this.$vuetify.breakpoint.name == 'xs')
                return "";
            return "4";
        }
    },
    methods: {
        sortProjects(category) {
            this.activeProjects = [];
            for (let project of this.projects) {
                for (let cat of project.categories) {
                    if (cat.name == category || category == 'Tous') {
                        this.activeProjects.push(project);
                        break;
                    }
                }
            }
        },
    },
    mounted () {
        this.$store.dispatch('loadCategories')
        .then(() => this.categories = this.$store.state.categories);

        this.$store.dispatch('loadProjects')
        .then(() => this.projects = this.$store.state.projects)
        .finally(() => this.sortProjects("Tous"));

    },
}
</script>
