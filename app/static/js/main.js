Vue.component('modal', {
    template: '#modal-template'
})


new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        images: null,
        loading: true,
        pageNumber: 0,
        size: 20
    },
    mounted() {
        this.updateImages();
    },
    computed: {
        pageCount() {
            let l = this.images.length,
                s = this.size;
            return Math.ceil(l / s);
        },
        paginatedData() {
            const start = this.pageNumber * this.size,
                end = start + this.size;
            return this.images.slice(start, end);
        }
    },
    methods: {
        nextPage() {
            this.pageNumber++;
        },
        prevPage() {
            this.pageNumber--;
        },
        updateImages() {
            axios
                .get('/api/get_images')
                .then(response => {
                    images = response.data.images;
                    for (let i = 0; i < images.length; i++) {
                        images[i].showModal = false;
                    }
                    this.images = images;
                })
                .catch(error => {
                    console.log(error);
                })
                .finally(() => (this.loading = false));
        },
        deleteImage(id) {
            axios
                .get('/api/delete_image?id=' + id)
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.log(error);
                })
                .finally(() => {
                    this.loading = true
                    this.updateImages();
                })
        }
    },
});
