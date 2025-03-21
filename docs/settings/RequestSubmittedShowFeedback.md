# Show Feedback form after Request Submission

**Technical Name:** RequestSubmittedShowFeedback

**Category:** Workflow

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** 

This parameter controls the visibility of a feedback form to the user immediately after a request has been submitted within the Pathlock GRC platform. Enabling this feature can collect immediate user feedback regarding their request submission experience.

**Business Impact:**

Enabling this feature can significantly improve the user experience by allowing immediate feedback after a request is submitted. It provides valuable insights to administrators for optimizing workflows and enhancing overall system usability and satisfaction.

**Technical Impact when configured:**

When enabled, a feedback form is displayed to the user right after a request submission, allowing for the collection of feedback directly related to the user's request experience. This can help in identifying potential areas of improvement within the request handling process or the platform's usability.

**Examples Scenario:**

- **User Satisfaction Measurement:** After submitting a security access request, a user is prompted to rate their experience or provide suggestions. This direct feedback can be used to streamline the process or clarify request submission guidelines.
  
**Related Settings:** 

- `RequestRecievedTemplate`
- `HomePageScreenForRedirectAfterLogin`

**Best Practices:** 

- **Configure when:** Gathering user feedback is essential for continuous improvement, especially after critical workflows such as access requests or incident reporting.
- **Avoid when:** If the request submission process is already optimized and additional feedback may not lead to significant improvements, or if the additional step might deter users from completing necessary actions due to perceived complexity.