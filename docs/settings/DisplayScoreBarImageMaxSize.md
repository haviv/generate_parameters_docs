**Technical Name:** DisplayScoreBarImageMaxSize

**Category:** Configuration

**Default Value:** Not explicitly mentioned in the provided references.

**Impact Level:** Medium

**Description:** This parameter defines the maximum allowable size for score bar images used within the Pathlock Cloud GRC platform. It is utilized to validate the dimensions of images to ensure they adhere to the platform's UI standards and performance expectations.

**Business Impact:** Proper configuration of this parameter ensures a consistent user experience by maintaining image size uniformity across the platform. It helps in preventing the display of oversized images that could distort UI elements or lead to longer page loading times, which might affect system performance and user satisfaction.

**Technical Impact when configured:** When configured, this parameter actively limits the size of images that can be uploaded or displayed within score bars. It ensures that only images with dimensions that fit within the specified maximum size are accepted, thereby optimizing both loading times and visual consistency across the platform.

**Example Scenario:** Consider a scenario where an administrator needs to upload a new score bar image to visually represent risk levels in a dashboard. If the image dimensions exceed the configured `DisplayScoreBarImageMaxSize`, the platform will reject the image, prompting the administrator to resize it to comply with the established limit. This ensures all score bar images across the platform maintain a uniform size, contributing to a cohesive visual experience.

**Related Settings:** Not explicitly mentioned in the provided references.

**Best Practices:** 
- **Configure when:** Setting up or updating the platform's UI, to ensure all images within the score bars are optimized for both performance and visual consistency.
- **Avoid when:** If there's a need to display images of varying sizes, which might not align with the goal of having a standardized UI appearance. However, careful consideration and testing should be applied to assess the impact on user experience and system performance.