<template>
  <div class="top">
    <h1 class="title">Japanese Company Name Generator</h1>
    <div class="input-area">
      <div class="input-area__keyword-area">
        <h2>Kerword</h2>
        <input v-model="fix_word" placeholder="Enter Kerword" />
        <p>Kerword is supposed to be only 1 word.</p>
        <p>Kerword is supposed to be Hiragana or Katakana or Kangi.</p>
        <p>Examples: あすと, デザイン, 情報</p>
      </div>
      <div class="input-area__length-area">
        <h2>Name Length: {{ length }}</h2>
        <input v-model="length" type="range" min="2" max="8" step="1" />
        <p>This is rough length assignment.</p>
      </div>
    </div>

    <button @click="submit">Generate</button>
    <div class="generated-area">
      <p class="generated-area__guide">Generated Name is</p>
      <p class="generated-area__generated">{{ generated }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  data() {
    return { fix_word: '', length: 4, generated: '...' }
  },
  methods: {
    async submit() {
      this.$nuxt.$loading.start()
      await axios
        .post('http://localhost:5005/api/generate', {
          length: Number(this.length),
          fix_word: this.fix_word
        })
        .then((response) => {
          this.generated = response.data
          this.$nuxt.$loading.finish()
        })
    }
  }
})
</script>

<style lang="scss" scoped>
.top {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  margin: 80px 0 70px;
}

.input-area {
  width: 80%;
  display: flex;
  justify-content: space-between;
  margin: 0 0 50px;

  &__keyword-area {
    width: 40%;
    background-color: #525bb9;
    padding: 30px;
    border-radius: 5px;
  }

  &__length-area {
    width: 40%;
    background-color: #525bb9;
    padding: 30px;
    border-radius: 5px;
  }
}
.generated-area {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  background-color: #525bb9;
  padding: 20px 80px 40px;
  border-radius: 5px;

  &__guide {
  }

  &__generated {
    margin: 0;
    font-size: 28px;
    font-weight: bold;
  }
}
</style>
