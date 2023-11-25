#!/usr/bin/env bash
#
# You should only work under the /scratch/users/<username> directory.
#
# Example job submission script
#
# -= Resources =-
#
#SBATCH --job-name=mandelbrot-jobs
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --partition=short
#SBATCH --time=00:30:00
#SBATCH --output=mandelbrot-jobs.out

################################################################################
##################### !!! DO NOT EDIT ABOVE THIS LINE !!! ######################
################################################################################
#SBATCH --qos=users
#SBATCH --account=users
#SBATCH --mail-type=END
#SBATCH --mail-user=kkacar20@ku.edu.tr

# Set stack size to unlimited
echo "Setting stack size to unlimited..."
ulimit -s unlimited
ulimit -l unlimited
ulimit -a
echo

echo "Running Job...!"
echo "==============================================================================="
echo "Running compiled binary..."

echo "Parallel version with 16 threads"
export OMP_NUM_THREADS=16
make -f ./mandelbrot/Makefile run
