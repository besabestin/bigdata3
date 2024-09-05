<template>
  <div>
	<ItemList :items="items" />
  </div>
</template>

<script>
import ItemList from '@/components/ItemList.vue';

export default {
  components: { ItemList },
  data() {
	return {
	  items: []
	};
  },
  methods: {
	async fetchItems() {
	  const response = await fetch('http://localhost:8003/items?bought=true');
	  this.items = await response.json();
	}
  },
  mounted() {
	this.fetchItems();
  }
};
</script>