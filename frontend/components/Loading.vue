<template lang="html">
  <div v-if="loading" class="loading-page">
    <img src="~/assets/loading.gif" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
@Component({})
export default class Loading extends Vue {
  protected loading: boolean = false

  public start() {
    this.loading = true
  }

  public finish() {
    this.loading = false
  }
}
</script>

<style lang="scss" scoped>
.loading-page {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding-top: 200px;
  font-size: 30px;
  font-family: sans-serif;
}
</style>
