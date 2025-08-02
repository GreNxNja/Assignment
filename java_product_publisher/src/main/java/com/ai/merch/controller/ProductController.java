
package com.ai.merch.controller;

import com.ai.merch.model.Product;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.UUID;

@RestController
@RequestMapping("/api/publish")
public class ProductController {

    @PostMapping
    public HashMap<String, String> publishProduct(@RequestBody Product product) {
        System.out.println("Received Product:");
        System.out.println("Title: " + product.getTitle());
        System.out.println("Description: " + product.getDescription());
        System.out.println("Tags: " + product.getTags());
        System.out.println("Image URL: " + product.getImageUrl());

        HashMap<String, String> response = new HashMap<>();
        response.put("fake_product_id", UUID.randomUUID().toString());
        return response;
    }
}
