public class OrderProcessor {
    public void processOrder(Order order) {
        // Step 1: Validate the order
        if (order == null || order.getItems().isEmpty()) {
            System.out.println("Invalid order.");
            return;
        }
        
        // Step 2: Calculate the total cost
        double total = 0;
        for (Item item : order.getItems()) {
            total += item.getPrice() * item.getQuantity();
        }
        
        // Step 3: Save the order to the database
        Database.save(order);
        
        // Step 4: Send confirmation email
        EmailService.sendEmail(order.getCustomerEmail(), "Order processed", "Your order total is $" + total);
    }
}
