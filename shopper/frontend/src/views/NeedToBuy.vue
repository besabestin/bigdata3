<template>
  <div>
	<ItemForm @item-added="fetchItems" />
	<ItemList :items="items" @item-updated="fetchItems" />
  </div>
</template>

<script>
import ItemForm from '@/components/ItemForm.vue';
import ItemList from '@/components/ItemList.vue';

export default {
  components: { ItemForm, ItemList },
  data() {
	return {
	  items: []
	};
  },
  methods: {
	async fetchItems() {
	  const response = await fetch('http://localhost:8003/items?bought=false');
	  this.items = await response.json();
	}
  },
  mounted() {
	this.fetchItems();
  }
};
</script>