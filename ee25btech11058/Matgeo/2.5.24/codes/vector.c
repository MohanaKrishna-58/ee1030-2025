#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Function to be compiled into a shared library (e.g., vector.so)
double angle_from_cross_c(double a, double b, double x, double y, double z) {
    double cross_mag_sq = x*x + y*y + z*z;
    double dot_prod_sq = (a*a * b*b) - cross_mag_sq;
    double dot_prod = sqrt(dot_prod_sq);
    double cos_theta = dot_prod / (a * b);
    double theta_rad = acos(cos_theta);
    return theta_rad * 180.0 / M_PI;
}