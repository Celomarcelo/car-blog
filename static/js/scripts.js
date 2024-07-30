document.addEventListener('DOMContentLoaded', function () {
    const saveButton = document.getElementById('save_changes');
    const profileForm = document.querySelector('form');
    let initialFormState = new FormData(profileForm);

    function checkFormChanges() {
        let currentFormState = new FormData(profileForm);
        let hasChanges = false;

        for (let [key, value] of currentFormState.entries()) {
            if (value !== initialFormState.get(key)) {
                hasChanges = true;
                break;
            }
        }

        saveButton.style.display = hasChanges ? 'inline-block' : 'none';
    }

    profileForm.addEventListener('input', checkFormChanges);
    profileForm.addEventListener('change', checkFormChanges);

    saveButton.style.display = 'none';
});