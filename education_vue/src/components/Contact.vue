<template>
    
    <section class="section">
      <div class="mb-6 px-6 py-4 has-background-grey-lighter">
        <h2 class="subtitle">Get In Touch</h2>
  
        <form @submit="submitForm">
        
          <div class="field">
            <label for="name">Name</label>
            <input type="text" class="input" id="name" v-model="contact.name">
          </div>
  
          <div class="field">
            <label for="email">Email</label>
            <input type="email" class="input" id="email" v-model="contact.email">
          </div>
  
          <div class="field">
            <label for="content">Content</label>
            <textarea class="textarea" id="content" v-model="contact.content"></textarea>
          </div>
  
          <div class="field buttons">
            <button class="button is-info" type="submit">Submit</button>
          </div>
        </form>
        
      </div>
    </section>
    <section class="section">
        
        
        <div class="mb-6 px-6 py-4 has-background-grey-lighter">
            <div class="columns is-multiline">
            <div class="column is-4">
                <div class="box has-text">
                    <h4 class="title is-4">Contact Information</h4>
                        <ul class="contact-list">
                            <li class="address">
                            <strong>Address 🏡 :</strong>
                            <span>198 West 21th Street, India</span>
                            </li><br>
                            <li class="phone">
                            <strong>Phone ☎ :</strong>
                            <a href="tel://9629547169">9627849329</a>
                            </li><br>
                            <li class="email">
                            <strong>Email 📧 :</strong>
                            <span></span>
                            <a href="mailto:asikahamed10@yahoo.com">education@gmail.com</a>
                            </li>
                        </ul>
                </div>
            </div>

            <div class="column is-4">
                <div class="box has-text">
                    <h4 class="title is-4">Learn & Grow</h4>
                        <ul class="contact-list">
                            <li class="address">
                            
                            <router-link to="/courses" class="navbar-item">📚 Courses</router-link>
                            </li>
                            <li class="phone">
                            
                            <router-link to="/projects" class="navbar-item">🎯 Projects</router-link>
                            </li>
                            <li class="phone">
                            
                            <router-link to="/projects" class="navbar-item">📰 Blogs</router-link>
                            </li>
                            
                        </ul>
                </div>
            </div>

            <div class="column is-4">
                <div class="box has-text">
                    <h4 class="title is-4">Our Services</h4>
                        <ul class="contact-list">

                            <li><a href="#">Web Design</a></li>
                            <li><a href="#">Web Development</a></li>
                            <li><a href="#">Online Courses</a></li>
                            <li><a href="#">Marketing</a></li>
                            <li><a href="#">Graphic Design</a></li>
                            
                        </ul>
                </div>
            </div>

            
            
        </div>
        </div>

        
        
  
    </section>
    
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: ['contact'],
    data() {
      return {
        errors: []
        
      };
    },
    methods: {

      submitForm() {
        console.log('submitForm')
  
        this.errors = [];
  
        if (this.contact.name === '') {
          this.errors.push('The name must be filled out');
        }
  
        if (this.contact.email === '') {
          this.errors.push('The email must be filled out');
        }
  
        if (this.contact.content === '') {
          this.errors.push('The content must be filled out');
        }

        
  
        if (!this.errors.length) {
          axios
            .post('/contact/', this.contact)

            .then(response => {
              this.contact.name = '';
              this.contact.email = '';
              this.contact.content = '';
              this.$emit('submitContact', response.data); // Change to 'submitContact'
            })
            .catch(error => {
              console.log(error);
            });
        }
      },
    },
  };
  </script>
  