Vue.component('modal', {
    template: '#modal-template'
})


new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        images: null,
        loading: true,
        images_on_page: null,
        size: 9,
    },
    created() {
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
            .finally(() => {
                this.loading = false;
                if (this.images.length > this.size) {
                    this.images_on_page = this.size;
                } else {
                    this.images_on_page = this.images.length;
                }
            });
    },
    mounted() {
        this.scroll();
    },
    computed: {
        imagesToShow() {
            return this.images.slice(0, this.images_on_page);
        }
    },
    methods: {
        scroll() {
            window.onscroll = () => {
                let closeToBottom = document.documentElement.scrollTop + window.innerHeight >= document.documentElement.offsetHeight - 50;
                if (closeToBottom) {
                    if (this.images_on_page <= this.images.length) {
                        this.showMoreImages();
                    }
                }
            }
        },
        showMoreImages() {
            if (this.images_on_page + this.size < this.images.length) {
                this.images_on_page += this.size;
            } else {
                this.images_on_page = this.images.length;
            }
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
                        .finally(() => {
                            this.loading = false;
                        });
                })
        }
    },
});
