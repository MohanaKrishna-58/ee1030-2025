#include <math.h>

// Must be global (not static) and not inside main()
double angle_between(double a, double b, double x, double y, double z) {
    double cross_mag = sqrt(x*x + y*y + z*z);
    double sin_theta = cross_mag / (a * b);
    double theta_rad = asin(sin_theta);
    return theta_rad * 180.0 / M_PI;
}
