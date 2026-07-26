import React from 'react';
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { useClerk, useUser } from '@clerk/nextjs';

import ProfilePage from '../app/profile/page';

const mockedUseUser = useUser as jest.Mock;
const mockedUseClerk = useClerk as jest.Mock;

describe('ProfilePage Component', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    global.mockNavigation.resetMocks();
  });

  test('renders authenticated Clerk user data and backend statistics', async () => {
    render(<ProfilePage />);

    expect(screen.getByText('Jane Cinema')).toBeInTheDocument();
    expect(screen.getByText('jane@example.com')).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.getByText('12')).toBeInTheDocument();
      expect(screen.getByText('4')).toBeInTheDocument();
    });

    expect(screen.getByText('Movies Watched')).toBeInTheDocument();
    expect(screen.getByText('Reviews')).toBeInTheDocument();
  });

  test('renders genre preferences in the taste radar', async () => {
    render(<ProfilePage />);

    await waitFor(() => {
      expect(
        screen.getByText('Your strongest movie preference is Science Fiction.'),
      ).toBeInTheDocument();
    });

    expect(screen.getByTestId('responsive-container')).toBeInTheDocument();
    expect(screen.getByTestId('radar-chart')).toBeInTheDocument();
    expect(screen.getByTestId('radar')).toBeInTheDocument();
  });

  test('opens Clerk user settings', () => {
    const openUserProfile = jest.fn();
    mockedUseClerk.mockReturnValue({ openUserProfile });

    render(<ProfilePage />);
    fireEvent.click(screen.getByRole('button', { name: 'Open profile settings' }));

    expect(openUserProfile).toHaveBeenCalledTimes(1);
  });

  test('redirects signed-out users to sign-in', async () => {
    mockedUseUser.mockReturnValue({
      isLoaded: true,
      isSignedIn: false,
      user: null,
    });

    render(<ProfilePage />);

    await waitFor(() => {
      expect(global.mockNavigation.replace).toHaveBeenCalledWith('/sign-in');
    });
  });
});
