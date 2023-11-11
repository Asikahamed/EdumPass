<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to EdumPass</h1>

        <h2 class="subtitle">The Great Aim of Education is not Knowledge, But Action</h2>
        <p class="subtitle">Brought to you by EdumPass</p>
        
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-clock"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">1-1 Doubt Clearance</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-comments"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">Industrial Projects</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">Lifetime content access</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">Job hunting techniques</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">Self paced learning</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>

              <h2 class="is-size-4 mt-4 mb-4">Free future updates</h2>

              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <a href="/sign-up" class="button is-info is-size-3 mt-6 mb-6">Click to get started</a>
          </div>

          <hr>

          <div 
              class="column is-3"
              v-for="course in courses"
              v-bind:key="course.id"
          >
              <CourseItem :course="course" />
          </div>
        </div>
      </div>
    </section>
    
   
    <section>
      
      <Contact :contact="contact"/>

    </section>
    <section class="contact-info">
  
</section>

  </div>
</template>

<script>
import axios from 'axios'

import CourseItem from '@/components/CourseItem.vue'
import Contact from '@/components/Contact.vue';

export default {
  name: 'Home',
  data() {
    return {
        courses: [],
        contact:[],
        
    };
  },

  components: {
      CourseItem,
      Contact
  },

  mounted() {
      console.log('mounted')

      document.title = 'Welcome | EdumPass'

      axios
          .get('courses/get_frontpage_courses/')
          .then(response => {
              console.log(response.data)

              this.courses = response.data
          })
  }
}
</script>


