# Custom Domain

**Technical Name:** CustomDomain

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Custom Domain parameter enables organizations to configure their Pathlock GRC platform to use a custom domain name. This is particularly useful for aligning the platform access with the organization's domain naming conventions, enhancing user experience and promoting a seamless integration with other organizational tools and systems.

**Business Impact:**

Using a custom domain for accessing the Pathlock GRC platform can significantly improve brand consistency and trustworthiness. It allows for a more professional appearance and can help in ensuring that employees recognize the platform as part of their daily workflow tools, potentially increasing adoption rates.

**Technical Impact when configured:**

- Ensures the platform is accessed through a recognizable, trusted URL that aligns with organizational policies.
- Can enhance security by facilitating the implementation of consistent security measures across all organizational tools.
- May require initial setup adjustments within your DNS provider and configuration changes within the Pathlock GRC platform to ensure seamless integration.

**Examples Scenario:**

A company named "Acme Corporation" wants their employees to access the Pathlock GRC platform via a URL that aligns with their other internal tools. Instead of using the default Pathlock provided domain, they configure a Custom Domain parameter to allow access via `grc.acme.com`. This alignment helps in making the platform easily recognizable to employees and reinforces the company's branding within their internal tools ecosystem.

**Related Settings:**

- SSL Certificate Configuration
- DNS Settings

**Best Practices:** configure when establishing a unified branding approach across all organizational IT systems; avoid when unnecessary, to keep the configuration simple and to reduce the potential for misconfiguration.