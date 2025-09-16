#include <stdio.h>
#include <math.h>

int main() {
    // Input magnitudes of vectors |a| and |b|
    double mag_a, mag_b;
    // Input cross product components a x b = (cx, cy, cz)
    double cx, cy, cz;

    // Take input
    scanf("%lf %lf", &mag_a, &mag_b);
    scanf("%lf %lf %lf", &cx, &cy, &cz);

    // Calculate magnitude of cross product vector
    double mag_cross = sqrt(cx*cx + cy*cy + cz*cz);

    // Use formula |a x b| = |a||b| sin(theta) to find sin(theta)
    double sin_theta = mag_cross / (mag_a * mag_b);

    // Calculate angle in radians
    double theta_rad = asin(sin_theta);

    // Convert to degrees
    double theta_deg = theta_rad * (180.0 / M_PI);

    // Output angle in degrees
    printf("%.2f\n", theta_deg);

    return 0;
}

