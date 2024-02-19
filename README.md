<h1>Project Description</h1>

<p>This project involves setting up a Django application with Django Rest Framework to create a single URL <code>/invoices/</code>. Below are the steps to accomplish this task:</p>

<ol>
  <li>
    <h2>Setup URL Patterns</h2>
    <p>Define the following URL patterns:</p>
    <ul>
      <li><code>/invoices/</code></li>
      <li><code>/invoices/&lt;int:pk&gt;/</code></li>
    </ul>
  </li>
  
  <li>
    <h2>Define Django Models</h2>
    <p>Create two Django models: Invoice and Invoice Detail.</p>
    
    <h3>Invoice Model Fields</h3>
    <ul>
      <li>Date</li>
      <li>Invoice Customer Name</li>
    </ul>
    
    <h3>Invoice Detail Model Fields</h3>
    <ul>
      <li>invoice (ForeignKey)</li>
      <li>Description</li>
      <li>Quantity</li>
      <li>Unit Price</li>
      <li>Price</li>
    </ul>
  </li>
  
  <li>
    <h2>Implement APIs</h2>
    <p>Utilize Django Rest Framework to develop APIs for handling all HTTP methods for the invoice models. The APIs should be capable of accepting invoice details in the payload and creating/updating the associated invoice details.</p>
  </li>
  
  <li>
    <h2>Develop Test Cases</h2>
    <p>Create test cases to thoroughly test all the API endpoints and ensure their functionality.</p>
  </li>
</ol>
