<template>
    <v-container fluid>
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
            projects: [
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/500/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/500/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/500/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/500/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/500/300',
                        alt: 'Photo non fournie',
                    },
                    title: "Testing",
                    description: 'Test description',
                    url: 'https://github.com/Aamsi/Portfolio'
                },
                {
                    image: {
                        source: 'https://picsum.photos/seed/picsum/500/300',
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