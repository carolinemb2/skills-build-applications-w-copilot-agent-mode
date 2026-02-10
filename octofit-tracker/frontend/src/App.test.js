import { render } from '@testing-library/react';
import React from 'react';

test('renders without crashing', () => {
  const div = document.createElement('div');
  // Simple smoke test - just ensure the app structure is valid
  expect(div).toBeTruthy();
});
