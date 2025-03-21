# Empty Profile Image New

**Technical Name:** EmptyProfileImage_New

**Category:** User Management

**Default Value:** null

**Impact Level:** Medium

**Description:**

This parameter is used to manage the default state of a user's profile image when no image is found or if the user has not set a profile image in the Pathlock Cloud GRC platform. It is part of the User Management settings, focusing on enhancing user profile management and visual consistency across the platform.

**Business Impact:**

Having a consistent and professional user interface, including default handling for empty profile images, impacts how users interact with the platform. A well-defined default state for profile images can lead to a more organized and visually appealing platform, enhancing the user experience and potentially improving platform adoption and usage.

**Technical Impact when configured:**

Configuring this parameter determines the fallback visualization for user profiles that lack an assigned or uploaded image. It ensures that even without individual user images, the user interface remains neat and professional, adhering to organizational visual standards.

**Examples Scenario:**

- **Recruiting:** In the recruiting module of Pathlock Cloud GRC, having a default profile image helps maintain a uniform appearance for all candidate profiles, especially when specific candidates haven’t uploaded a picture.
- **User Directory:** In a vast user directory, setting a default image for users without a specific photo helps prevent visual inconsistency, which could otherwise make the user directory feel less organized.

**Related Settings:** 

- `EmploymentStatusForActiveEmployee`
- `EmploymentStatusForNotFound`

**Best Practices:** 

- **Configure when:** It's crucial to set a default profile image that aligns with your company's branding and professional standards. This ensures that every user profile, even those without an uploaded image, maintains a consistent and professional appearance.
  
- **Avoid when:** If your organization has specific requirements that allow for individual expression through profile images, or if there is a policy that mandates users to upload a personal image, relying on a default image might be less necessary.