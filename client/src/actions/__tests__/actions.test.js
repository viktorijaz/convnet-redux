import mockAxios from "axios";
import configureMockStore from 'redux-mock-store'
import thunk from 'redux-thunk'
import * as actions from '../index'
import * as types from '../types'

const middlewares = [thunk]
const mockStore = configureMockStore(middlewares)

describe('async actions', () => {


    const store = mockStore({ images: [] })

    it('should run fetchImages() and test for axios call', () => {
        const mockImpl = mockAxios.get.mockImplementation((arg) =>
            Promise.resolve({
                'response': {
	                'data': {
	                        'images': ["cute.jpg"]
	                }
                }
            })
        );

        const expectedActions = [
            { type: types.FETCH_IMAGES }
        ]
        return store.dispatch(actions.fetchImages()).then(() => {
            expect(store.getActions()).toEqual(expectedActions)
        })
    })
})