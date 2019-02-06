const mockAxios = jest.genMockFromModule('axios')

export default {
  get: jest.fn(() => Promise.resolve({ response: {data: [] }})),
  create: jest.fn(() => mockAxios)
};