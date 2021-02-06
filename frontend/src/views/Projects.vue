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
                ></v-select>
            </v-col>
        </v-row>

        <v-row dense>
            <v-col
                v-for="project in projects"
                :key="project.title"
            >
                <Project
                    :image="project.image"
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
    data() {
        return {
            categories: [],
            projects: [
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/300/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/300/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/300/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/300/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
            ]
        }
    }
}
</script>

<style lang="scss">

</style>