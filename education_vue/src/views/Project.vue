<template>
    <div class="project">
      <section class="section">
        <div class="container">
          <div class="columns content">
            <div class="column is-2">
              <!-- You can add a table of contents here if needed -->
            </div>
  
            <div class="column is-10">
                <template v-if="project.lesson_type === 'video'">
                    <Video
                        v-bind:youtube_id="project.youtube_id"
                    />
                </template>

              <hr>
  
              <template v-if="project">
                <h2>Project Description</h2>
                <div v-html="project.long_description"></div>
              </template>
              <template v-else>
                <h2>Description not available</h2>
              </template>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import Video from '@/components/Video';
  import axios from 'axios';
  
  export default {
    components: {
      Video
    },
    data() {
      return {
        project: {
            title: '',
            lesson_type: ''
        }
      };
    },
    async mounted() {
      console.log('mounted');
  
      const slug = this.$route.params.slug;
  
      await axios
        .get(`projects/${slug}/`)
        .then(response => {
          console.log(response.data);
  
          this.project = response.data.project;
          this.lessons = response.data.lessons;
        });
  
      document.title = this.project.title + ' | EdumPass';
    }
  };
  </script>
  