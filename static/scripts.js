document.addEventListener('DOMContentLoaded', () => {
    // Function to update the current date and time
    function updateTime() {
        const now = new Date();
        const dateTimeString = now.toLocaleDateString() + ' ' + now.toLocaleTimeString();
        document.getElementById('date-time').textContent = dateTimeString;
    }
    setInterval(updateTime, 1000);
    updateTime();

    const salesForm = document.getElementById('salesForm');
    const productNameSelect = document.getElementById('productName');
    const productPriceInput = document.getElementById('productPrice');

    productNameSelect.addEventListener('change', (event) => {
        const selectedOption = event.target.selectedOptions[0];
        const price = selectedOption.getAttribute('data-price');
        productPriceInput.value = price ? parseFloat(price).toFixed(2) : '';
    });

    salesForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(salesForm);

        fetch('/add_sale', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('totalSales').textContent = data.total_sales.toFixed(2);
            document.getElementById('cumulativeSales').textContent = data.cumulative_sales.toFixed(2);
        })
        .catch(error => console.error('Error:', error));

        // Clear the form
        salesForm.reset();
    });
});
