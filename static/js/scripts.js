document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('save_changes');
    const profileForm = document.querySelector('form');
    let initialFormState = new FormData(profileForm);

    function checkFormChanges() {
        let currentFormState = new FormData(profileForm);
        for (let [key, value] of currentFormState.entries()) {
            if (value !== initialFormState.get(key)) {
                saveButton.style.display = 'inline-block';
                return;
            }
        }
        saveButton.style.display = 'none';
    }

    profileForm.addEventListener('input', checkFormChanges);
    profileForm.addEventListener('change', checkFormChanges);
});