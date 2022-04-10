<template>
    <form @submit.prevent="uploadPhoto" id="uploadForm" method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" name="description"></textarea>
        </div>

        <div class="form-group">
            <label for="photo" class="custom-file-label">Upload photo</label>
            <input class="form-control-file" type="file" name="photo" />
        </div>

        <button class="btn btn-primary" type="submit" name="submit"> Submit </button>

    </form>

</template>

<script>

export default {
    data(){
        return {
            csrf_token: ''
        };
    }, 

    created() {
        this.getCsrfToken();
    },
    
    methods: {
        uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);

            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })
                .then(function (response){
                    return response.json();
                })
                .then(function (data) {
                    //display a success message
                    console.log(data);
                })
                .catch(function (error) {
                    console.log(error);
                });
        },

        getCsrfToken() {
            let self = this;
            fetch("/api/csrf-token")
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                })
        }
    }

}

</script>

<style>
.form-group{
    max-width: 50%;
    margin-bottom: 15px;
} 

label{
    font-size: 16px;
}

</style>
