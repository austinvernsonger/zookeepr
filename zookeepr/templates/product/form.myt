<p><label for="product.category">Category</label>
<select name="product.category">
% for category in c.product_categories:
  <option value="<%category.id%>"><% category.name %></option>
% #endfor
</select>
</p>

<p><label for="product.active">Active:</label>
<% h.check_box('product.active') %></p>

<p><label for="product.description">Description:</label><br>
<% h.textfield('product.description') %></p>

<p><label for="product.cost">Cost (in cents. ie $100 = 10000):</label><br>
<% h.textfield('product.cost') %></p>

<p><label for="product.auth">Auth code:</label><br>
<% h.textfield('product.auth') %></p>

<p><label for="product.validate">Validate code:</label><br>
<% h.textfield('product.validate') %></p>