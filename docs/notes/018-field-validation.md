# Field Validation

Domain: healthcare research

This note records an implementation detail for Clinical Trial Screen. The current operating
threshold is `0.69` and review should happen within `72` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
