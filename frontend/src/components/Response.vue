<template>
  <v-container class="ma-0">
    <v-card max-width="86%" color="background" v-if="data">
      <v-card-title class="green">Response</v-card-title>
      <v-card-text>
        <v-card>
          <v-card-text>
            <vue-json-pretty :data="data"/>
          </v-card-text>
        </v-card>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { api } from "~api"
import VueJsonPretty from 'vue-json-pretty';
import 'vue-json-pretty/lib/styles.css';

export default {
  name: "Response",
  components: {
    VueJsonPretty
  },
  props: {
    params: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      data: null,
    }
  },
  watch: {
    params: {
      handler: "makeRequest",
      deep: true,
    },
  },
  methods: {
    async makeRequest() {
      this.data = await api.request(this.params)
      this.$emit("beesCounter")
    }
  },
  mounted() {
    this.makeRequest()
  }
}
</script>

<style>
.green {
  color: #50fa7b;
}
</style>
