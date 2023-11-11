<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img :src="project.get_image" alt="Placeholder image">
            </figure>
        </div>

        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <p class="is-size-5">{{ project.title }}</p>
                </div>
            </div>

            <div class="content">
                <p>{{ project.short_description }}</p>

                <router-link :to="{name: 'Project', params: {slug: project.slug}}">More</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['project']
}
</script>