<template>
    <Project
        :image="{
            source: 'https://i.picsum.photos/id/76/200/200.jpg?hmac=psXm-BMm4NaZlO_dAn3FH6ahWyqXeDxPEkz5hU8XVqM',
            alt: 'Photo non fournie'
        }"
        :title="'Test'"
        :description="'Test description'"
        :url="'https://github.com/Aamsi/Portfolio'"
    />
</template>

<script>
import Project from '../components/Project'

export default {
    name: 'Projects',
    components: {
        Project,
    }
}
</script>