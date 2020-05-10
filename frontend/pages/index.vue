<template>
  <div>
    <h1>Japanese Company Name Generator</h1>
    <div>
      <p>Kerword</p>
      <p>※Kerword is supposed to be only 1 word.</p>
      <p>※Kerword is supposed to be Hiragana or Katakana or Kangi.</p>
      <p>Example1: あすと</p>
      <p>Example2: デザイン</p>
      <p>Example3: 情報</p>
      <input v-model="fix_word" placeholder="Enter Kerword" />
    </div>
    <div>
      <p>Number of Words: {{ length }}</p>
      <input v-model="length" type="range" min="2" max="8" step="1" />
    </div>
    <button @click="submit">Generate</button>
    <p>Generated Name: {{ test }}</p>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  data() {
    return { fix_word: '', length: 4, test: '' }
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
          this.test = response.data
          this.$nuxt.$loading.finish()
        })
    }
  }
})
</script>

<style lang="scss" scoped></style>
