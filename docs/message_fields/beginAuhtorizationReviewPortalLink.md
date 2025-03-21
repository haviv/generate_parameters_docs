**Field Name:** beginAuhtorizationReviewPortalLink

**Description:** The `beginAuhtorizationReviewPortalLink` field represents a placeholder within email templates that is used to generate a hyperlink directing users to the Authorization Review Portal in Pathlock Cloud. It is used to provide recipients with easy access to begin or review authorization processes directly from their email.

**Usage Context:** This field is typically used in email templates related to workflow processes, specifically when notifying users about tasks requiring them to access the Authorization Review Portal. It is employed in scenarios where recipients need to verify or review authorization details, ensuring they have a direct link to the relevant portal page.

**Example:**

    Visit the Authorization Review Portal: $$beginAuhtorizationReviewPortalLink$$

    After rendering:

    Visit the Authorization Review Portal: 
    <a href="https://cloud.pathlock.com/AuthorizationReviewPortal">Authorization Review Portal</a>