<template>
    
    <div v-if="success_msg" class="alert alert-success">
        {{ success_msg }}
    </div>
    <div v-else-if="errors.length" class="alert alert-danger">
        <ul>
            <li v-for="error in errors">{{ error }}</li>
        </ul>
    </div>


    <form @submit.prevent="uploadPhoto" id="uploadForm" method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" name="description"></textarea>
        </div>

        <div class="form-group d-flex flex-column">
            <label for="photo">Upload photo</label>
            <input class="form-control-file" type="file" name="photo" />
        </div>

        <button class="btn btn-primary" type="submit" name="submit"> Submit </button>

    </form>

</template>

<script>

export default {
    data(){
        return {
            csrf_token: '',
            errors: [],
            success_msg: ''
        };
    }, 

    created() {
        this.getCsrfToken();
    },
    
    methods: {
        uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            let self = this;

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
                    self.errors = data.errors;
                    self.success_msg = data.message;
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
    margin-bottom: 15px;
} 

label{
    font-size: 16px;
    margin-botton: 10px;
}

</style>
