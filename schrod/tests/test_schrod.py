from unittest import TestCase
import schrod.schrod as schrod
import numpy as np



# ----- Helper functions -----
def issorted(x):
    """Check if x is sorted"""
    return (np.diff(x) >= 0).all()

# ----- The tests -----
class TestSchrod(TestCase):

    def test_noisy_convergence_nbasis(self):
        """
        Test to see if the eigenvalues converge with increasing number of
        basis states.
        """

        # ----- Setup -----
        # The x grid
        n_x = 200
        x_min = -3
        x_max = 3
        x_vec = np.linspace(x_min, x_max, n_x)

        # The potentials
        n_V = 10
        sig = 2
        V_rand = np.random.normal(0, sig, (n_V,n_x) )

        # Schrodinger equations
        n_init = 20
        n_max = 200
        seq = schrod.Schrod(x_vec, V_rand, n_init)

        # Number of eigenvalues to check =
        n_eig_check = 10 # n_eig_check <= n_init

        # The initial truncation
        eigs = seq.solve()[0][:,0:n_eig_check]

        # increase the basis size until failure
        # or test_tol is achieved
        test_tol =1e-6
        measured_tol = 1 # the max rel. err. of the eigenvalues
        n = n_init
        step = 5
        passed = False
        while measured_tol >= test_tol and n <= n_max:
            n+=step
            seq.set_n_basis(n)
            eigs_new = seq.solve()[0][:,0:n_eig_check]

            measured_tol = np.mean(np.abs((eigs - eigs_new) / 0.5 / (eigs + eigs_new)))
            eigs = eigs_new

            if measured_tol <= test_tol:
                passed = True

        if not passed:
            self.fail()

    def test_convergence_boxsize(self):
        """Test to see if the eigenvalues converge with increasing box size."""
        self.fail()

    def test_accuracy_eig_vals(self):
        """Test the accuracy of the eigenvalues for several known cases."""
        self.fail()

    def test_accuracy_eig_vecs(self):
        """Test the accuracy of the eigenvectors for several known cases."""
        self.fail()

