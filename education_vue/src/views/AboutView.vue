<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">About</h1>
      </div>
    </div>
    <br>
    
    <!-- About Section -->
    <section class="about-section">
      <div class="container">
        <div class="columns is-vcentered">
          <div class="column is-6">
            <h2 class="title is-2 custom-blue">Welcome to Education</h2><br>
              <p>Welcome to our online learning platform, where we are dedicated to helping students in their final year projects and providing a wide range of online courses for upskilling.</p><br>
              <p>We understand the challenges that final year students face when it comes to their academic projects. Our platform offers guidance, resources, and expert mentorship to ensure your project's success.</p><br>
              <p>For those looking to enhance their skills and knowledge, we offer a variety of online courses covering a wide range of subjects. Whether you want to learn programming, business, design, or any other skill, we have you covered.</p><br>
              <p>We understand the challenges that final year students face when it comes to their academic projects. Our platform offers guidance, resources, and expert mentorship to ensure your project's success.</p><br>
              <p>For those looking to enhance their skills and knowledge, we offer a variety of online courses covering a wide range of subjects. Whether you want to learn programming, business, design, or any other skill, we have you covered.</p>
          </div>
          <div class="column is-6">
            <img src="/E-learning.jpeg" alt="About Us" />
          </div>
        </div>
      </div>
      <div class="container">
  <div class="columns is-vcentered">
    <div class="column is-6">
      <img src="/project.jpeg" alt="About Us" />
    </div>
    <div class="column is-6">
      
      <p>Welcome to our online learning platform, where we are dedicated to helping students in their final year projects and providing a wide range of online courses for upskilling.</p><br>
      <p>We understand the challenges that final year students face when it comes to their academic projects. Our platform offers guidance, resources, and expert mentorship to ensure your project's success.</p><br>
      <p>For those looking to enhance their skills and knowledge, we offer a variety of online courses covering a wide range of subjects. Whether you want to learn programming, business, design, or any other skill, we have you covered.</p><br>
      <p>We understand the challenges that final year students face when it comes to their academic projects. Our platform offers guidance, resources, and expert mentorship to ensure your project's success.</p><br>
      
    </div>
  </div>
</div>

   </section>
  <br>

    <!-- Why Choose Us Section -->
    <section class="about-section">
      <div class="container">
        <h2 class="title is-2 custom-blue">Why Choose Us</h2>
        <div class="columns is-multiline">
          <div class="column is-6" v-for="point in chooseUsPoints" :key="point.id">
            <div class="box">
              <h5 class="title is-5">{{ point.title }}</h5>
              <p>{{ point.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <br>
    <br>

    <!-- Project Streams Section -->
    <section class="project-streams">
      <div class="container">
        <h4 class="title is-4 custom-blue">Explore Our Project Streams</h4>
        <div class="columns is-multiline">
          <div class="column is-6" v-for="stream in projectStreams" :key="stream.id">
            <div class="project-stream">
              <h5 class="title is-5">{{ stream.title }}</h5>
              <p>{{ stream.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <br>

    <!-- Web Development Courses Section -->
    <section class="web-dev-courses">
      <div class="container">
        <h4 class="title is-4 custom-blue">Explore Our Courses</h4>
        <div class="columns is-multiline">
          <div class="column is-6" v-for="course in webDevCourses" :key="course.id">
            <div class="course-card">
              <h5 class="title is-5">{{ course.title }}</h5>
              <p>{{ course.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <br>

    <!-- Programming Courses Section -->
    <section class="programming-courses">
      <div class="container">
        <h5 class="title is-5">Explore Programming Courses</h5>
        <div class="columns is-multiline">
          <div class="column is-6" v-for="course in programmingCourses" :key="course.id">
            <div class="course-card">
              <h5 class="title is-5">{{ course.title }}</h5>
              <p>{{ course.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chooseUsPoints: [
        {
          id: 1,
          title: "Experienced Team",
          description: "Our team consists of experienced professionals dedicated to guiding students and learners on their educational journey."
        },
        {
          id: 2,
          title: "Flexible Learning",
          description: "We offer flexible learning options, allowing you to access our content and courses at your own pace and schedule."
        },
        {
          id: 3,
          title: "Practical Knowledge",
          description: "Our courses and projects are designed to provide practical knowledge and skills that can be applied in real-world scenarios."
        },
        {
          id: 4,
          title: "Community Support",
          description: "Join a supportive community of learners and mentors who are passionate about education and personal growth."
        }
      ],
      projectStreams: [
        {
          id: 1,
          title: "Software Projects",
          description: "Dive into the world of software development with our software project stream. Create web applications, mobile apps, and software solutions that solve real-world problems."
        },
        {
          id: 2,
          title: "Machine Learning Projects",
          description: "Explore the fascinating field of machine learning. Work on projects that leverage AI and data science to make predictions, automate tasks, and gain insights from data."
        },
        {
          id: 3,
          title: "Electronics Projects",
          description: "Get hands-on experience in electronics and hardware projects. Build circuits, design electronic systems, and create innovative electronic devices."
        },
        {
          id: 4,
          title: "Python Projects",
          description: "Develop practical Python projects that range from web development and automation to data analysis and more. Python is a versatile and powerful language for various applications."
        }
      ],
      webDevCourses: [
        {
          id: 1,
          title: "Web Development Basics",
          description: "Learn the fundamentals of web development, including HTML, CSS, and JavaScript."
        },
        {
          id: 2,
          title: "Responsive Web Design",
          description: "Dive into responsive web design, ensuring your websites look great on all devices."
        },
        {
          id: 3,
          title: "JavaScript Mastery",
          description: "Master JavaScript, the programming language of the web, and build interactive web apps."
        }
      ],
      programmingCourses: [
        {
          id: 1,
          title: "Python Programming",
          description: "Learn Python, a versatile programming language used in web development, data analysis, and more."
        },
        {
          id: 2,
          title: "Java for Beginners",
          description: "Dive into Java programming and start your journey in software development."
        },
        {
          id: 3,
          title: "C++ Essentials",
          description: "Learn the essentials of C++, a powerful programming language used in game development and systems programming."
        }
      ]
    };
  },
  mounted() {
    document.title = 'About | EdumPass';
  }
}
</script>


<style scoped>
.custom-blue {
  color: rgb(0, 162, 255);
}
</style>